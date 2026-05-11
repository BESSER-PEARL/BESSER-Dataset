





import java.util.List;
import java.util.ArrayList;

public class mpl_Operation  {

    private String name;





    private List<mpl_VariableDeclaration> mpl_variabledeclarations;




    private mpl_MPLModel mpl_mplmodel;




    private mpl_Block mpl_block;




    private List<mpl_VariableDeclaration> mpl_variabledeclarations;




    private mpl_OperationCall mpl_operationcall;


    public mpl_Operation(
        String name    ) {
        this.name = name;
        this.mpl_variabledeclarations = new ArrayList<>();
        this.mpl_variabledeclarations = new ArrayList<>();
    }

    public mpl_Operation(
        String name        ArrayList<mpl_VariableDeclaration> mpl_variabledeclarations,        ArrayList<mpl_VariableDeclaration> mpl_variabledeclarations    ) {
        this.name = name;
        this.mpl_variabledeclarations = mpl_variabledeclarations;
        this.mpl_variabledeclarations = mpl_variabledeclarations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<mpl_VariableDeclaration> getMpl_variabledeclarations() {
        return mpl_variabledeclarations;
    }

    public void addMpl_variabledeclaration(Mpl_variabledeclaration mpl_variabledeclaration) {
        this.mpl_variabledeclarations.add(mpl_variabledeclaration);
    }
    public mpl_MPLModel getMpl_mplmodel() {
        return mpl_mplmodel;
    }

    public void setMpl_mplmodel(mpl_MPLModel mpl_mplmodel) {
        this.mpl_mplmodel = mpl_mplmodel;
    }
    public mpl_Block getMpl_block() {
        return mpl_block;
    }

    public void setMpl_block(mpl_Block mpl_block) {
        this.mpl_block = mpl_block;
    }
    public List<mpl_VariableDeclaration> getMpl_variabledeclarations() {
        return mpl_variabledeclarations;
    }

    public void addMpl_variabledeclaration(Mpl_variabledeclaration mpl_variabledeclaration) {
        this.mpl_variabledeclarations.add(mpl_variabledeclaration);
    }
    public mpl_OperationCall getMpl_operationcall() {
        return mpl_operationcall;
    }

    public void setMpl_operationcall(mpl_OperationCall mpl_operationcall) {
        this.mpl_operationcall = mpl_operationcall;
    }

}