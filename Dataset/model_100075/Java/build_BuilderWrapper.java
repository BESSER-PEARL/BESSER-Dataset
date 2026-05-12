





import java.util.List;
import java.util.ArrayList;

public class build_BuilderWrapper extends IBuilder, BFunctionWrapper {

    private boolean inputAdvised;
    private boolean providesAdvised;
    private boolean sourceAdvised;
    private boolean unitTypeAdvised;
    private boolean defaultPropertiesAdvised;
    private boolean outputAdvised;



    public build_BuilderWrapper(
        boolean inputAdvised,        boolean providesAdvised,        boolean sourceAdvised,        boolean unitTypeAdvised,        boolean defaultPropertiesAdvised,        boolean outputAdvised    ) {
        super(
        );
        this.inputAdvised = inputAdvised;
        this.providesAdvised = providesAdvised;
        this.sourceAdvised = sourceAdvised;
        this.unitTypeAdvised = unitTypeAdvised;
        this.defaultPropertiesAdvised = defaultPropertiesAdvised;
        this.outputAdvised = outputAdvised;
    }


    public boolean getInputadvised() {
        return inputAdvised;
    }

    public void setInputadvised(boolean inputAdvised) {
        this.inputAdvised = inputAdvised;
    }
    public boolean getProvidesadvised() {
        return providesAdvised;
    }

    public void setProvidesadvised(boolean providesAdvised) {
        this.providesAdvised = providesAdvised;
    }
    public boolean getSourceadvised() {
        return sourceAdvised;
    }

    public void setSourceadvised(boolean sourceAdvised) {
        this.sourceAdvised = sourceAdvised;
    }
    public boolean getUnittypeadvised() {
        return unitTypeAdvised;
    }

    public void setUnittypeadvised(boolean unitTypeAdvised) {
        this.unitTypeAdvised = unitTypeAdvised;
    }
    public boolean getDefaultpropertiesadvised() {
        return defaultPropertiesAdvised;
    }

    public void setDefaultpropertiesadvised(boolean defaultPropertiesAdvised) {
        this.defaultPropertiesAdvised = defaultPropertiesAdvised;
    }
    public boolean getOutputadvised() {
        return outputAdvised;
    }

    public void setOutputadvised(boolean outputAdvised) {
        this.outputAdvised = outputAdvised;
    }


}