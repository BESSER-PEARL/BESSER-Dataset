





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLPrintingSetup_PageSetup  {






    private Layout layout;




    private Header header;




    private Footer footer;




    private WorksheetOptionsElt worksheetoptionselt;


    public SpreadsheetMLPrintingSetup_PageSetup(
    ) {
    }



    public Layout getLayout() {
        return layout;
    }

    public void setLayout(Layout layout) {
        this.layout = layout;
    }
    public Header getHeader() {
        return header;
    }

    public void setHeader(Header header) {
        this.header = header;
    }
    public Footer getFooter() {
        return footer;
    }

    public void setFooter(Footer footer) {
        this.footer = footer;
    }
    public WorksheetOptionsElt getWorksheetoptionselt() {
        return worksheetoptionselt;
    }

    public void setWorksheetoptionselt(WorksheetOptionsElt worksheetoptionselt) {
        this.worksheetoptionselt = worksheetoptionselt;
    }

}