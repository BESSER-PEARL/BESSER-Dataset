





import java.util.List;
import java.util.ArrayList;

public class setup_ContextVariableTask extends SetupTask {

    private String name;
    private boolean stringSubstitution;
    private String value;
    private String label;
    private String type;



    public setup_ContextVariableTask(
        String name,        boolean stringSubstitution,        String value,        String label,        String type    ) {
        super(
        );
        this.name = name;
        this.stringSubstitution = stringSubstitution;
        this.value = value;
        this.label = label;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getStringsubstitution() {
        return stringSubstitution;
    }

    public void setStringsubstitution(boolean stringSubstitution) {
        this.stringSubstitution = stringSubstitution;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}