





import java.util.List;
import java.util.ArrayList;

public class myAtl_LetVariableCS  {

    private String name;





    private myAtl_TypeExpCS myatl_typeexpcs;




    private myAtl_LetExpCS myatl_letexpcs;




    private myAtl_ExpCS myatl_expcs;


    public myAtl_LetVariableCS(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myAtl_TypeExpCS getMyatl_typeexpcs() {
        return myatl_typeexpcs;
    }

    public void setMyatl_typeexpcs(myAtl_TypeExpCS myatl_typeexpcs) {
        this.myatl_typeexpcs = myatl_typeexpcs;
    }
    public myAtl_LetExpCS getMyatl_letexpcs() {
        return myatl_letexpcs;
    }

    public void setMyatl_letexpcs(myAtl_LetExpCS myatl_letexpcs) {
        this.myatl_letexpcs = myatl_letexpcs;
    }
    public myAtl_ExpCS getMyatl_expcs() {
        return myatl_expcs;
    }

    public void setMyatl_expcs(myAtl_ExpCS myatl_expcs) {
        this.myatl_expcs = myatl_expcs;
    }

}