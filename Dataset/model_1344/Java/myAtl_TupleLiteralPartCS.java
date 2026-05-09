





import java.util.List;
import java.util.ArrayList;

public class myAtl_TupleLiteralPartCS  {

    private String name;





    private myAtl_TupleLiteralExpCS myatl_tupleliteralexpcs;




    private myAtl_ExpCS myatl_expcs;




    private myAtl_TypeExpCS myatl_typeexpcs;


    public myAtl_TupleLiteralPartCS(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myAtl_TupleLiteralExpCS getMyatl_tupleliteralexpcs() {
        return myatl_tupleliteralexpcs;
    }

    public void setMyatl_tupleliteralexpcs(myAtl_TupleLiteralExpCS myatl_tupleliteralexpcs) {
        this.myatl_tupleliteralexpcs = myatl_tupleliteralexpcs;
    }
    public myAtl_ExpCS getMyatl_expcs() {
        return myatl_expcs;
    }

    public void setMyatl_expcs(myAtl_ExpCS myatl_expcs) {
        this.myatl_expcs = myatl_expcs;
    }
    public myAtl_TypeExpCS getMyatl_typeexpcs() {
        return myatl_typeexpcs;
    }

    public void setMyatl_typeexpcs(myAtl_TypeExpCS myatl_typeexpcs) {
        this.myatl_typeexpcs = myatl_typeexpcs;
    }

}