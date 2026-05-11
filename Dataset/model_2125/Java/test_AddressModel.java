




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class test_AddressModel  {

    private boolean differentPostAddress;
    private LocalDate validTo;
    private String houseNumber;
    private LocalDate validFrom;
    private String zipCode;
    private String street;



    public test_AddressModel(
        boolean differentPostAddress,        LocalDate validTo,        String houseNumber,        LocalDate validFrom,        String zipCode,        String street    ) {
        this.differentPostAddress = differentPostAddress;
        this.validTo = validTo;
        this.houseNumber = houseNumber;
        this.validFrom = validFrom;
        this.zipCode = zipCode;
        this.street = street;
    }


    public boolean getDifferentpostaddress() {
        return differentPostAddress;
    }

    public void setDifferentpostaddress(boolean differentPostAddress) {
        this.differentPostAddress = differentPostAddress;
    }
    public LocalDate getValidto() {
        return validTo;
    }

    public void setValidto(LocalDate validTo) {
        this.validTo = validTo;
    }
    public String getHousenumber() {
        return houseNumber;
    }

    public void setHousenumber(String houseNumber) {
        this.houseNumber = houseNumber;
    }
    public LocalDate getValidfrom() {
        return validFrom;
    }

    public void setValidfrom(LocalDate validFrom) {
        this.validFrom = validFrom;
    }
    public String getZipcode() {
        return zipCode;
    }

    public void setZipcode(String zipCode) {
        this.zipCode = zipCode;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }


}