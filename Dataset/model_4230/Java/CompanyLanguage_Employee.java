





import java.util.List;
import java.util.ArrayList;

public class CompanyLanguage_Employee  {

    private String name;





    private CompanyLanguage_CEO companylanguage_ceo;


    public CompanyLanguage_Employee(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public CompanyLanguage_CEO getCompanylanguage_ceo() {
        return companylanguage_ceo;
    }

    public void setCompanylanguage_ceo(CompanyLanguage_CEO companylanguage_ceo) {
        this.companylanguage_ceo = companylanguage_ceo;
    }

}