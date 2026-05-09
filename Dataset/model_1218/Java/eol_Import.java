





import java.util.List;
import java.util.ArrayList;

public class eol_Import extends EOLElement {

    private String imported;



    public eol_Import(
        String imported    ) {
        super(
        );
        this.imported = imported;
    }


    public String getImported() {
        return imported;
    }

    public void setImported(String imported) {
        this.imported = imported;
    }


}