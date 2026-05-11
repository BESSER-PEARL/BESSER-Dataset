





import java.util.List;
import java.util.ArrayList;

public class customers_CanadaAddress extends Address {

    private String province;



    public customers_CanadaAddress(
        String province    ) {
        super(
        );
        this.province = province;
    }


    public String getProvince() {
        return province;
    }

    public void setProvince(String province) {
        this.province = province;
    }


}