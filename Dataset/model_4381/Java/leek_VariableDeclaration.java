





import java.util.List;
import java.util.ArrayList;

public class leek_VariableDeclaration extends ForInitializer, ForInVariableReference {

    private boolean byAdress;
    private String name;





    private leek_GlobalDeclaration leek_globaldeclaration;




    private leek_FunctionDeclaration leek_functiondeclaration;




    private leek_LocalDeclaration leek_localdeclaration;


    public leek_VariableDeclaration(
        boolean byAdress,        String name    ) {
        super(
        );
        this.byAdress = byAdress;
        this.name = name;
    }


    public boolean getByadress() {
        return byAdress;
    }

    public void setByadress(boolean byAdress) {
        this.byAdress = byAdress;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public leek_GlobalDeclaration getLeek_globaldeclaration() {
        return leek_globaldeclaration;
    }

    public void setLeek_globaldeclaration(leek_GlobalDeclaration leek_globaldeclaration) {
        this.leek_globaldeclaration = leek_globaldeclaration;
    }
    public leek_FunctionDeclaration getLeek_functiondeclaration() {
        return leek_functiondeclaration;
    }

    public void setLeek_functiondeclaration(leek_FunctionDeclaration leek_functiondeclaration) {
        this.leek_functiondeclaration = leek_functiondeclaration;
    }
    public leek_LocalDeclaration getLeek_localdeclaration() {
        return leek_localdeclaration;
    }

    public void setLeek_localdeclaration(leek_LocalDeclaration leek_localdeclaration) {
        this.leek_localdeclaration = leek_localdeclaration;
    }

}