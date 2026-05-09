





import java.util.List;
import java.util.ArrayList;

public class myDsl_RelationArch  {

    private String name;
    private String target;
    private String source;





    private myDsl_Architecture mydsl_architecture;


    public myDsl_RelationArch(
        String name,        String target,        String source    ) {
        this.name = name;
        this.target = target;
        this.source = source;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public myDsl_Architecture getMydsl_architecture() {
        return mydsl_architecture;
    }

    public void setMydsl_architecture(myDsl_Architecture mydsl_architecture) {
        this.mydsl_architecture = mydsl_architecture;
    }

}