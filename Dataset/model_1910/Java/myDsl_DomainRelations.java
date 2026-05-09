





import java.util.List;
import java.util.ArrayList;

public class myDsl_DomainRelations  {

    private String name;





    private myDsl_DomainConnection mydsl_domainconnection;




    private List<myDsl_EObject> mydsl_eobjects;


    public myDsl_DomainRelations(
        String name    ) {
        this.name = name;
        this.mydsl_eobjects = new ArrayList<>();
    }

    public myDsl_DomainRelations(
        String name        ArrayList<myDsl_EObject> mydsl_eobjects    ) {
        this.name = name;
        this.mydsl_eobjects = mydsl_eobjects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_DomainConnection getMydsl_domainconnection() {
        return mydsl_domainconnection;
    }

    public void setMydsl_domainconnection(myDsl_DomainConnection mydsl_domainconnection) {
        this.mydsl_domainconnection = mydsl_domainconnection;
    }
    public List<myDsl_EObject> getMydsl_eobjects() {
        return mydsl_eobjects;
    }

    public void addMydsl_eobject(Mydsl_eobject mydsl_eobject) {
        this.mydsl_eobjects.add(mydsl_eobject);
    }

}