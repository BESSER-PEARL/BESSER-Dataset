





import java.util.List;
import java.util.ArrayList;

public class SPL_StructureDeclaration extends Declaration {






    private List<SPL_Argument> spl_arguments;


    public SPL_StructureDeclaration(
    ) {
        super(
        );
        this.spl_arguments = new ArrayList<>();
    }

    public SPL_StructureDeclaration(
        ArrayList<SPL_Argument> spl_arguments    ) {
        this.spl_arguments = spl_arguments;
    }


    public List<SPL_Argument> getSpl_arguments() {
        return spl_arguments;
    }

    public void addSpl_argument(Spl_argument spl_argument) {
        this.spl_arguments.add(spl_argument);
    }

}