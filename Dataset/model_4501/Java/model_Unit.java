





import java.util.List;
import java.util.ArrayList;

public class model_Unit  {

    private boolean isIntervalScaled;
    private String symbol;
    private boolean isRatioScaled;
    private String name;
    private boolean isBaseUnit;
    private boolean isDerivedUnit;
    private boolean isCoherentDerivedUnit;





    private model_Quantity model_quantity;


    public model_Unit(
        boolean isIntervalScaled,        String symbol,        boolean isRatioScaled,        String name,        boolean isBaseUnit,        boolean isDerivedUnit,        boolean isCoherentDerivedUnit    ) {
        this.isIntervalScaled = isIntervalScaled;
        this.symbol = symbol;
        this.isRatioScaled = isRatioScaled;
        this.name = name;
        this.isBaseUnit = isBaseUnit;
        this.isDerivedUnit = isDerivedUnit;
        this.isCoherentDerivedUnit = isCoherentDerivedUnit;
    }


    public boolean getIsintervalscaled() {
        return isIntervalScaled;
    }

    public void setIsintervalscaled(boolean isIntervalScaled) {
        this.isIntervalScaled = isIntervalScaled;
    }
    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public boolean getIsratioscaled() {
        return isRatioScaled;
    }

    public void setIsratioscaled(boolean isRatioScaled) {
        this.isRatioScaled = isRatioScaled;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public boolean getIscoherentderivedunit() {
        return isCoherentDerivedUnit;
    }

    public void setIscoherentderivedunit(boolean isCoherentDerivedUnit) {
        this.isCoherentDerivedUnit = isCoherentDerivedUnit;
    }

    public model_Quantity getModel_quantity() {
        return model_quantity;
    }

    public void setModel_quantity(model_Quantity model_quantity) {
        this.model_quantity = model_quantity;
    }

}