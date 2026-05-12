





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLPrintingSetup_Worksheet  {

    private String protected;
    private String rightToLeft;
    private String name;



    public SpreadsheetMLPrintingSetup_Worksheet(
        String protected,        String rightToLeft,        String name    ) {
        this.protected = protected;
        this.rightToLeft = rightToLeft;
        this.name = name;
    }


    public String getProtected() {
        return protected;
    }

    public void setProtected(String protected) {
        this.protected = protected;
    }
    public String getRighttoleft() {
        return rightToLeft;
    }

    public void setRighttoleft(String rightToLeft) {
        this.rightToLeft = rightToLeft;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}