





import java.util.List;
import java.util.ArrayList;

public class muddle_Feature  {

    private boolean primary;
    private String name;
    private boolean runtime;
    private boolean many;



    public muddle_Feature(
        boolean primary,        String name,        boolean runtime,        boolean many    ) {
        this.primary = primary;
        this.name = name;
        this.runtime = runtime;
        this.many = many;
    }


    public boolean getPrimary() {
        return primary;
    }

    public void setPrimary(boolean primary) {
        this.primary = primary;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getRuntime() {
        return runtime;
    }

    public void setRuntime(boolean runtime) {
        this.runtime = runtime;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }


}