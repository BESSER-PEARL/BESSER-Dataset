





import java.util.List;
import java.util.ArrayList;

public class TypeGraphTrace_Trace  {






    private List<TypeGraphTrace_ClassListTrace> typegraphtrace_classlisttraces;


    public TypeGraphTrace_Trace(
    ) {
        this.typegraphtrace_classlisttraces = new ArrayList<>();
    }

    public TypeGraphTrace_Trace(
        ArrayList<TypeGraphTrace_ClassListTrace> typegraphtrace_classlisttraces    ) {
        this.typegraphtrace_classlisttraces = typegraphtrace_classlisttraces;
    }


    public List<TypeGraphTrace_ClassListTrace> getTypegraphtrace_classlisttraces() {
        return typegraphtrace_classlisttraces;
    }

    public void addTypegraphtrace_classlisttrace(Typegraphtrace_classlisttrace typegraphtrace_classlisttrace) {
        this.typegraphtrace_classlisttraces.add(typegraphtrace_classlisttrace);
    }

}