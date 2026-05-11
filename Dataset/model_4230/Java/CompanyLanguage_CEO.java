





import java.util.List;
import java.util.ArrayList;

public class CompanyLanguage_CEO  {

    private String name;





    private CompanyLanguage_Admin companylanguage_admin;


    public CompanyLanguage_CEO(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public CompanyLanguage_Admin getCompanylanguage_admin() {
        return companylanguage_admin;
    }

    public void setCompanylanguage_admin(CompanyLanguage_Admin companylanguage_admin) {
        this.companylanguage_admin = companylanguage_admin;
    }

}