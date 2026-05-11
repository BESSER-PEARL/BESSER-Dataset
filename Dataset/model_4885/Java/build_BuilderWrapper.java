





import java.util.List;
import java.util.ArrayList;

public class build_BuilderWrapper extends IBuilder, BFunctionWrapper {

    private boolean sourceAdvised;
    private boolean providesAdvised;
    private boolean defaultPropertiesAdvised;
    private boolean unitTypeAdvised;
    private boolean outputAdvised;
    private boolean inputAdvised;



    public build_BuilderWrapper(
        boolean sourceAdvised,        boolean providesAdvised,        boolean defaultPropertiesAdvised,        boolean unitTypeAdvised,        boolean outputAdvised,        boolean inputAdvised    ) {
        super(
        );
        this.sourceAdvised = sourceAdvised;
        this.providesAdvised = providesAdvised;
        this.defaultPropertiesAdvised = defaultPropertiesAdvised;
        this.unitTypeAdvised = unitTypeAdvised;
        this.outputAdvised = outputAdvised;
        this.inputAdvised = inputAdvised;
    }


    public boolean getSourceadvised() {
        return sourceAdvised;
    }

    public void setSourceadvised(boolean sourceAdvised) {
        this.sourceAdvised = sourceAdvised;
    }
    public boolean getProvidesadvised() {
        return providesAdvised;
    }

    public void setProvidesadvised(boolean providesAdvised) {
        this.providesAdvised = providesAdvised;
    }
    public boolean getDefaultpropertiesadvised() {
        return defaultPropertiesAdvised;
    }

    public void setDefaultpropertiesadvised(boolean defaultPropertiesAdvised) {
        this.defaultPropertiesAdvised = defaultPropertiesAdvised;
    }
    public boolean getUnittypeadvised() {
        return unitTypeAdvised;
    }

    public void setUnittypeadvised(boolean unitTypeAdvised) {
        this.unitTypeAdvised = unitTypeAdvised;
    }
    public boolean getOutputadvised() {
        return outputAdvised;
    }

    public void setOutputadvised(boolean outputAdvised) {
        this.outputAdvised = outputAdvised;
    }
    public boolean getInputadvised() {
        return inputAdvised;
    }

    public void setInputadvised(boolean inputAdvised) {
        this.inputAdvised = inputAdvised;
    }


}