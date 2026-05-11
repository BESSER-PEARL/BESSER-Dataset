





import java.util.List;
import java.util.ArrayList;

public class co2_PackageDeclaration  {

    private String name;
    private boolean single;





    private co2_CO2System co2_co2system;


    public co2_PackageDeclaration(
        String name,        boolean single    ) {
        this.name = name;
        this.single = single;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getSingle() {
        return single;
    }

    public void setSingle(boolean single) {
        this.single = single;
    }

    public co2_CO2System getCo2_co2system() {
        return co2_co2system;
    }

    public void setCo2_co2system(co2_CO2System co2_co2system) {
        this.co2_co2system = co2_co2system;
    }

}