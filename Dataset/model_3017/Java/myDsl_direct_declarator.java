





import java.util.List;
import java.util.ArrayList;

public class myDsl_direct_declarator  {

    private String name;





    private myDsl_declarator mydsl_declarator;




    private myDsl_direct_declarator2 mydsl_direct_declarator2;




    private myDsl_declarator mydsl_declarator;


    public myDsl_direct_declarator(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_declarator getMydsl_declarator() {
        return mydsl_declarator;
    }

    public void setMydsl_declarator(myDsl_declarator mydsl_declarator) {
        this.mydsl_declarator = mydsl_declarator;
    }
    public myDsl_direct_declarator2 getMydsl_direct_declarator2() {
        return mydsl_direct_declarator2;
    }

    public void setMydsl_direct_declarator2(myDsl_direct_declarator2 mydsl_direct_declarator2) {
        this.mydsl_direct_declarator2 = mydsl_direct_declarator2;
    }
    public myDsl_declarator getMydsl_declarator() {
        return mydsl_declarator;
    }

    public void setMydsl_declarator(myDsl_declarator mydsl_declarator) {
        this.mydsl_declarator = mydsl_declarator;
    }

}