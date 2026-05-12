





import java.util.List;
import java.util.ArrayList;

public class publication_Journal extends BiblioReference {

    private String iSSN;



    public publication_Journal(
        String iSSN    ) {
        super(
        );
        this.iSSN = iSSN;
    }


    public String getIssn() {
        return iSSN;
    }

    public void setIssn(String iSSN) {
        this.iSSN = iSSN;
    }


}