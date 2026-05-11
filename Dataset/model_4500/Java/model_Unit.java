





import java.util.List;
import java.util.ArrayList;

public class model_Unit  {

    private boolean isCoherentDerivedUnit;
    private boolean isBaseUnit;
    private boolean isDerivedUnit;
    private boolean isIntervalScaled;
    private boolean isRatioScaled;
    private String symbol;
    private String name;





    private model_Quantity model_quantity;


    public model_Unit(
        boolean isCoherentDerivedUnit,        boolean isBaseUnit,        boolean isDerivedUnit,        boolean isIntervalScaled,        boolean isRatioScaled,        String symbol,        String name    ) {
        this.isCoherentDerivedUnit = isCoherentDerivedUnit;
        this.isBaseUnit = isBaseUnit;
        this.isDerivedUnit = isDerivedUnit;
        this.isIntervalScaled = isIntervalScaled;
        this.isRatioScaled = isRatioScaled;
        this.symbol = symbol;
        this.name = name;
    }


    public boolean getIscoherentderivedunit() {
        return isCoherentDerivedUnit;
    }

    public void setIscoherentderivedunit(boolean isCoherentDerivedUnit) {
        this.isCoherentDerivedUnit = isCoherentDerivedUnit;
    }
    public boolean getIsbaseunit() {
        return isBaseUnit;
    }

    public void setIsbaseunit(boolean isBaseUnit) {
        this.isBaseUnit = isBaseUnit;
    }
    public boolean getIsderivedunit() {
        return isDerivedUnit;
    }

    public void setIsderivedunit(boolean isDerivedUnit) {
        this.isDerivedUnit = isDerivedUnit;
    }
    public boolean getIsintervalscaled() {
        return isIntervalScaled;
    }

    public void setIsintervalscaled(boolean isIntervalScaled) {
        this.isIntervalScaled = isIntervalScaled;
    }
    public boolean getIsratioscaled() {
        return isRatioScaled;
    }

    public void setIsratioscaled(boolean isRatioScaled) {
        this.isRatioScaled = isRatioScaled;
    }
    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_Quantity getModel_quantity() {
        return model_quantity;
    }

    public void setModel_quantity(model_Quantity model_quantity) {
        this.model_quantity = model_quantity;
    }

}