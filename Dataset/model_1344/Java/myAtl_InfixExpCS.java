





import java.util.List;
import java.util.ArrayList;

public class myAtl_InfixExpCS extends InfixedExpCS {






    private List<myAtl_PrefixedExpCS> myatl_prefixedexpcss;




    private List<myAtl_BinaryOperatorCS> myatl_binaryoperatorcss;


    public myAtl_InfixExpCS(
    ) {
        super(
        );
        this.myatl_prefixedexpcss = new ArrayList<>();
        this.myatl_binaryoperatorcss = new ArrayList<>();
    }

    public myAtl_InfixExpCS(
        ArrayList<myAtl_PrefixedExpCS> myatl_prefixedexpcss,        ArrayList<myAtl_BinaryOperatorCS> myatl_binaryoperatorcss    ) {
        this.myatl_prefixedexpcss = myatl_prefixedexpcss;
        this.myatl_binaryoperatorcss = myatl_binaryoperatorcss;
    }


    public List<myAtl_PrefixedExpCS> getMyatl_prefixedexpcss() {
        return myatl_prefixedexpcss;
    }

    public void addMyatl_prefixedexpcs(Myatl_prefixedexpcs myatl_prefixedexpcs) {
        this.myatl_prefixedexpcss.add(myatl_prefixedexpcs);
    }
    public List<myAtl_BinaryOperatorCS> getMyatl_binaryoperatorcss() {
        return myatl_binaryoperatorcss;
    }

    public void addMyatl_binaryoperatorcs(Myatl_binaryoperatorcs myatl_binaryoperatorcs) {
        this.myatl_binaryoperatorcss.add(myatl_binaryoperatorcs);
    }

}