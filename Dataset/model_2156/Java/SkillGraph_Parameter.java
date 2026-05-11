





import java.util.List;
import java.util.ArrayList;

public class SkillGraph_Parameter  {

    private boolean variable;
    private String abbreviation;
    private String defaultValue;
    private String name;
    private String unit;



    public SkillGraph_Parameter(
        boolean variable,        String abbreviation,        String defaultValue,        String name,        String unit    ) {
        this.variable = variable;
        this.abbreviation = abbreviation;
        this.defaultValue = defaultValue;
        this.name = name;
        this.unit = unit;
    }


    public boolean getVariable() {
        return variable;
    }

    public void setVariable(boolean variable) {
        this.variable = variable;
    }
    public String getAbbreviation() {
        return abbreviation;
    }

    public void setAbbreviation(String abbreviation) {
        this.abbreviation = abbreviation;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}