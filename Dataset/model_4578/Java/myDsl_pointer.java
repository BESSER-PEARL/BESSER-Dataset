





import java.util.List;
import java.util.ArrayList;

public class myDsl_pointer extends abstract_declarator {






    private myDsl_declarator mydsl_declarator;




    private List<myDsl_pointer> mydsl_pointers;


    public myDsl_pointer(
    ) {
        super(
        );
        this.mydsl_pointers = new ArrayList<>();
    }

    public myDsl_pointer(
        ArrayList<myDsl_pointer> mydsl_pointers    ) {
        this.mydsl_pointers = mydsl_pointers;
    }


    public myDsl_declarator getMydsl_declarator() {
        return mydsl_declarator;
    }

    public void setMydsl_declarator(myDsl_declarator mydsl_declarator) {
        this.mydsl_declarator = mydsl_declarator;
    }
    public List<myDsl_pointer> getMydsl_pointers() {
        return mydsl_pointers;
    }

    public void addMydsl_pointer(Mydsl_pointer mydsl_pointer) {
        this.mydsl_pointers.add(mydsl_pointer);
    }

}