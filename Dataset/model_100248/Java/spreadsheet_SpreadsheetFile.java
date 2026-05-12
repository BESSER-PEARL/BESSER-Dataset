





import java.util.List;
import java.util.ArrayList;

public class spreadsheet_SpreadsheetFile extends DocumentModel {

    private int nbSheet;



    public spreadsheet_SpreadsheetFile(
        int nbSheet    ) {
        super(
        );
        this.nbSheet = nbSheet;
    }


    public int getNbsheet() {
        return nbSheet;
    }

    public void setNbsheet(int nbSheet) {
        this.nbSheet = nbSheet;
    }


}