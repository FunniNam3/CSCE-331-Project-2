
import java.awt.*;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.file.Paths;
import java.sql.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;
import javax.swing.*;

public class XReportPanel extends JPanel {

    // ==========================================================
    private GUI gui;
    private static Connection conn;

    public XReportPanel(GUI gui) {
        this.gui = gui;
        setLayout(new BorderLayout());
        getConnection();

        createTopBar();
        getSales();
    }

    // ===================== TOP BAR =====================
    private void createTopBar() {

        JPanel topBar = new JPanel(new FlowLayout(FlowLayout.LEFT));

        JButton backButton = new JButton("Menu");
        backButton.addActionListener(e -> gui.showScreen("MAIN"));
        topBar.add(backButton);

        add(topBar, BorderLayout.NORTH);
    }

    // Get connection to database
    private static void getConnection() {

        Properties props = new Properties();
        var envFile = Paths.get(".env").toAbsolutePath().toString();

        try (FileInputStream inputStream = new FileInputStream(envFile)) {
            props.load(inputStream);
        } catch (IOException e) {
            System.err.println("Error loading .env file: " + e.getMessage());
            return;
        }

        try {
            String databaseUrl = props.getProperty("DATABASE_URL") + props.getProperty("DATABASE_NAME");
            String databaseUser = props.getProperty("DATABASE_USER");
            String databasePassword = props.getProperty("DATABASE_PASSWORD");

            conn = DriverManager.getConnection(
                    databaseUrl,
                    databaseUser,
                    databasePassword
            );

        } catch (SQLException e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }
    }

    private void getSales() {
        String salesQuery = """
SELECT * 
FROM receipt 
WHERE purchase_date >= CURRENT_DATE 
  AND purchase_date < ?;
""";
        try {

            LocalDateTime myDateObj = LocalDateTime.now();
            DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
            String formattedDate = myDateObj.format(myFormatObj);

            PreparedStatement stmt = conn.prepareStatement(salesQuery);
            stmt.setTimestamp(1, Timestamp.valueOf(formattedDate));

            ResultSet result = stmt.executeQuery();

            System.out.println(result);

        } catch (SQLException e) {
            JOptionPane.showMessageDialog(this, e.getMessage());
        }
    }
}
