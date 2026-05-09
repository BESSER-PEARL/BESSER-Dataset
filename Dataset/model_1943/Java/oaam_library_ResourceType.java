





import java.util.List;
import java.util.ArrayList;

public class oaam_library_ResourceType extends common_OaamBaseElementA, library_ResourceConsumerA {

    private String direction;
    private boolean isIo;
    private boolean isDistinguishable;
    private String unit;
    private boolean isConsumed;
    private boolean isPropagated;
    private boolean isConfigurable;



    public oaam_library_ResourceType(
        String direction,        boolean isIo,        boolean isDistinguishable,        String unit,        boolean isConsumed,        boolean isPropagated,        boolean isConfigurable    ) {
        super(
        );
        this.direction = direction;
        this.isIo = isIo;
        this.isDistinguishable = isDistinguishable;
        this.unit = unit;
        this.isConsumed = isConsumed;
        this.isPropagated = isPropagated;
        this.isConfigurable = isConfigurable;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public boolean getIsio() {
        return isIo;
    }

    public void setIsio(boolean isIo) {
        this.isIo = isIo;
    }
    public boolean getIsdistinguishable() {
        return isDistinguishable;
    }

    public void setIsdistinguishable(boolean isDistinguishable) {
        this.isDistinguishable = isDistinguishable;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public boolean getIsconsumed() {
        return isConsumed;
    }

    public void setIsconsumed(boolean isConsumed) {
        this.isConsumed = isConsumed;
    }
    public boolean getIspropagated() {
        return isPropagated;
    }

    public void setIspropagated(boolean isPropagated) {
        this.isPropagated = isPropagated;
    }
    public boolean getIsconfigurable() {
        return isConfigurable;
    }

    public void setIsconfigurable(boolean isConfigurable) {
        this.isConfigurable = isConfigurable;
    }


}