





import java.util.List;
import java.util.ArrayList;

public class df_Unit extends Attributable {

    private String name;
    private int lineNumber;
    private String fileName;



    public df_Unit(
        String name,        int lineNumber,        String fileName    ) {
        super(
        );
        this.name = name;
        this.lineNumber = lineNumber;
        this.fileName = fileName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getLinenumber() {
        return lineNumber;
    }

    public void setLinenumber(int lineNumber) {
        this.lineNumber = lineNumber;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }


}