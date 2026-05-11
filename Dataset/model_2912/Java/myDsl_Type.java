





import java.util.List;
import java.util.ArrayList;

public class myDsl_Type  {

    private String name;





    private myDsl_DomainModel mydsl_domainmodel;


    public myDsl_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_DomainModel getMydsl_domainmodel() {
        return mydsl_domainmodel;
    }

    public void setMydsl_domainmodel(myDsl_DomainModel mydsl_domainmodel) {
        this.mydsl_domainmodel = mydsl_domainmodel;
    }

}