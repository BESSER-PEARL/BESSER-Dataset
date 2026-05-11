





import java.util.List;
import java.util.ArrayList;

public class build_BuilderInputDecorator extends BuilderInput {






    private List<build_BuilderInput> build_builderinputs;


    public build_BuilderInputDecorator(
    ) {
        super(
        );
        this.build_builderinputs = new ArrayList<>();
    }

    public build_BuilderInputDecorator(
        ArrayList<build_BuilderInput> build_builderinputs    ) {
        this.build_builderinputs = build_builderinputs;
    }


    public List<build_BuilderInput> getBuild_builderinputs() {
        return build_builderinputs;
    }

    public void addBuild_builderinput(Build_builderinput build_builderinput) {
        this.build_builderinputs.add(build_builderinput);
    }

}