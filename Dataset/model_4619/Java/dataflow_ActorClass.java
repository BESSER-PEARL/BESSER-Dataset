





import java.util.List;
import java.util.ArrayList;

public class dataflow_ActorClass extends Attributable {

    private String name;
    private String nameSpace;
    private String sourceCode;
    private String sourceFile;





    private List<dataflow_Actor> dataflow_actors;




    private dataflow_Actor dataflow_actor;


    public dataflow_ActorClass(
        String name,        String nameSpace,        String sourceCode,        String sourceFile    ) {
        super(
        );
        this.name = name;
        this.nameSpace = nameSpace;
        this.sourceCode = sourceCode;
        this.sourceFile = sourceFile;
        this.dataflow_actors = new ArrayList<>();
    }

    public dataflow_ActorClass(
        String name,        String nameSpace,        String sourceCode,        String sourceFile        ArrayList<dataflow_Actor> dataflow_actors    ) {
        this.name = name;
        this.nameSpace = nameSpace;
        this.sourceCode = sourceCode;
        this.sourceFile = sourceFile;
        this.dataflow_actors = dataflow_actors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNamespace() {
        return nameSpace;
    }

    public void setNamespace(String nameSpace) {
        this.nameSpace = nameSpace;
    }
    public String getSourcecode() {
        return sourceCode;
    }

    public void setSourcecode(String sourceCode) {
        this.sourceCode = sourceCode;
    }
    public String getSourcefile() {
        return sourceFile;
    }

    public void setSourcefile(String sourceFile) {
        this.sourceFile = sourceFile;
    }

    public List<dataflow_Actor> getDataflow_actors() {
        return dataflow_actors;
    }

    public void addDataflow_actor(Dataflow_actor dataflow_actor) {
        this.dataflow_actors.add(dataflow_actor);
    }
    public dataflow_Actor getDataflow_actor() {
        return dataflow_actor;
    }

    public void setDataflow_actor(dataflow_Actor dataflow_actor) {
        this.dataflow_actor = dataflow_actor;
    }

}