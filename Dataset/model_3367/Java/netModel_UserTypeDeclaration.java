





import java.util.List;
import java.util.ArrayList;

public class netModel_UserTypeDeclaration extends Declaration {

    private String keyword;
    private boolean nogen;



    public netModel_UserTypeDeclaration(
        String keyword,        boolean nogen    ) {
        super(
        );
        this.keyword = keyword;
        this.nogen = nogen;
    }


    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }
    public boolean getNogen() {
        return nogen;
    }

    public void setNogen(boolean nogen) {
        this.nogen = nogen;
    }


}