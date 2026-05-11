





import java.util.List;
import java.util.ArrayList;

public class myDsl_Namespace extends Element {

    private String name;





    private List<myDsl_Element> mydsl_elements;


    public myDsl_Namespace(
        String name    ) {
        super(
        );
        this.name = name;
        this.mydsl_elements = new ArrayList<>();
    }

    public myDsl_Namespace(
        String name        ArrayList<myDsl_Element> mydsl_elements    ) {
        this.name = name;
        this.mydsl_elements = mydsl_elements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<myDsl_Element> getMydsl_elements() {
        return mydsl_elements;
    }

    public void addMydsl_element(Mydsl_element mydsl_element) {
        this.mydsl_elements.add(mydsl_element);
    }

}