





import java.util.List;
import java.util.ArrayList;

public class Java5_VariableDeclarationStatement extends Statement {

    private int extraArrayDimensions;





    private List<Java5_VariableDeclarationFragment> java5_variabledeclarationfragments;




    private Java5_VariableDeclarationFragment java5_variabledeclarationfragment;


    public Java5_VariableDeclarationStatement(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
        this.java5_variabledeclarationfragments = new ArrayList<>();
    }

    public Java5_VariableDeclarationStatement(
        int extraArrayDimensions        ArrayList<Java5_VariableDeclarationFragment> java5_variabledeclarationfragments    ) {
        this.extraArrayDimensions = extraArrayDimensions;
        this.java5_variabledeclarationfragments = java5_variabledeclarationfragments;
    }

    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }

    public List<Java5_VariableDeclarationFragment> getJava5_variabledeclarationfragments() {
        return java5_variabledeclarationfragments;
    }

    public void addJava5_variabledeclarationfragment(Java5_variabledeclarationfragment java5_variabledeclarationfragment) {
        this.java5_variabledeclarationfragments.add(java5_variabledeclarationfragment);
    }
    public Java5_VariableDeclarationFragment getJava5_variabledeclarationfragment() {
        return java5_variabledeclarationfragment;
    }

    public void setJava5_variabledeclarationfragment(Java5_VariableDeclarationFragment java5_variabledeclarationfragment) {
        this.java5_variabledeclarationfragment = java5_variabledeclarationfragment;
    }

}