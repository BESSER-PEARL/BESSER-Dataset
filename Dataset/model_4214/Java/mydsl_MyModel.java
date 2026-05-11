





import java.util.List;
import java.util.ArrayList;

public class mydsl_MyModel  {

    private String name;





    private List<mydsl_MyAbstractElement> mydsl_myabstractelements;


    public mydsl_MyModel(
        String name    ) {
        this.name = name;
        this.mydsl_myabstractelements = new ArrayList<>();
    }

    public mydsl_MyModel(
        String name        ArrayList<mydsl_MyAbstractElement> mydsl_myabstractelements    ) {
        this.name = name;
        this.mydsl_myabstractelements = mydsl_myabstractelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<mydsl_MyAbstractElement> getMydsl_myabstractelements() {
        return mydsl_myabstractelements;
    }

    public void addMydsl_myabstractelement(Mydsl_myabstractelement mydsl_myabstractelement) {
        this.mydsl_myabstractelements.add(mydsl_myabstractelement);
    }

}