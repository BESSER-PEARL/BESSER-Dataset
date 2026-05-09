





import java.util.List;
import java.util.ArrayList;

public class transformr_Block extends Executable {






    private List<transformr_Executable> transformr_executables;


    public transformr_Block(
    ) {
        super(
        );
        this.transformr_executables = new ArrayList<>();
    }

    public transformr_Block(
        ArrayList<transformr_Executable> transformr_executables    ) {
        this.transformr_executables = transformr_executables;
    }


    public List<transformr_Executable> getTransformr_executables() {
        return transformr_executables;
    }

    public void addTransformr_executable(Transformr_executable transformr_executable) {
        this.transformr_executables.add(transformr_executable);
    }

}