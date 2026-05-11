





import java.util.List;
import java.util.ArrayList;

public class xal_AddressLine  {

    private String mixed;
    private String code;
    private String type;
    private String anyAttribute;





    private xal_SubPremise xal_subpremise;




    private xal_ThoroughfareNumberRange xal_thoroughfarenumberrange;




    private xal_ThoroughfareNumberTo xal_thoroughfarenumberto;




    private xal_Country xal_country;




    private xal_AddressLines xal_addresslines;




    private xal_PremiseNumberRangeTo xal_premisenumberrangeto;




    private xal_ThoroughfareNumberFrom xal_thoroughfarenumberfrom;




    private xal_Locality xal_locality;




    private xal_AdministrativeArea xal_administrativearea;




    private xal_PremiseNumberRangeFrom xal_premisenumberrangefrom;




    private xal_Thoroughfare xal_thoroughfare;


    public xal_AddressLine(
        String mixed,        String code,        String type,        String anyAttribute    ) {
        this.mixed = mixed;
        this.code = code;
        this.type = type;
        this.anyAttribute = anyAttribute;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }

    public xal_SubPremise getXal_subpremise() {
        return xal_subpremise;
    }

    public void setXal_subpremise(xal_SubPremise xal_subpremise) {
        this.xal_subpremise = xal_subpremise;
    }
    public xal_ThoroughfareNumberRange getXal_thoroughfarenumberrange() {
        return xal_thoroughfarenumberrange;
    }

    public void setXal_thoroughfarenumberrange(xal_ThoroughfareNumberRange xal_thoroughfarenumberrange) {
        this.xal_thoroughfarenumberrange = xal_thoroughfarenumberrange;
    }
    public xal_ThoroughfareNumberTo getXal_thoroughfarenumberto() {
        return xal_thoroughfarenumberto;
    }

    public void setXal_thoroughfarenumberto(xal_ThoroughfareNumberTo xal_thoroughfarenumberto) {
        this.xal_thoroughfarenumberto = xal_thoroughfarenumberto;
    }
    public xal_Country getXal_country() {
        return xal_country;
    }

    public void setXal_country(xal_Country xal_country) {
        this.xal_country = xal_country;
    }
    public xal_AddressLines getXal_addresslines() {
        return xal_addresslines;
    }

    public void setXal_addresslines(xal_AddressLines xal_addresslines) {
        this.xal_addresslines = xal_addresslines;
    }
    public xal_PremiseNumberRangeTo getXal_premisenumberrangeto() {
        return xal_premisenumberrangeto;
    }

    public void setXal_premisenumberrangeto(xal_PremiseNumberRangeTo xal_premisenumberrangeto) {
        this.xal_premisenumberrangeto = xal_premisenumberrangeto;
    }
    public xal_ThoroughfareNumberFrom getXal_thoroughfarenumberfrom() {
        return xal_thoroughfarenumberfrom;
    }

    public void setXal_thoroughfarenumberfrom(xal_ThoroughfareNumberFrom xal_thoroughfarenumberfrom) {
        this.xal_thoroughfarenumberfrom = xal_thoroughfarenumberfrom;
    }
    public xal_Locality getXal_locality() {
        return xal_locality;
    }

    public void setXal_locality(xal_Locality xal_locality) {
        this.xal_locality = xal_locality;
    }
    public xal_AdministrativeArea getXal_administrativearea() {
        return xal_administrativearea;
    }

    public void setXal_administrativearea(xal_AdministrativeArea xal_administrativearea) {
        this.xal_administrativearea = xal_administrativearea;
    }
    public xal_PremiseNumberRangeFrom getXal_premisenumberrangefrom() {
        return xal_premisenumberrangefrom;
    }

    public void setXal_premisenumberrangefrom(xal_PremiseNumberRangeFrom xal_premisenumberrangefrom) {
        this.xal_premisenumberrangefrom = xal_premisenumberrangefrom;
    }
    public xal_Thoroughfare getXal_thoroughfare() {
        return xal_thoroughfare;
    }

    public void setXal_thoroughfare(xal_Thoroughfare xal_thoroughfare) {
        this.xal_thoroughfare = xal_thoroughfare;
    }

}