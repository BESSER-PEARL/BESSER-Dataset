




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_ETypes  {

    private String eLong;
    private LocalDate eDate;
    private String eBigInteger;
    private String eShort;
    private String eBigDecimal;
    private float eFloat;
    private float eDouble;
    private String eByte;
    private int eInt;
    private boolean eBoolean;
    private String eString;
    private String eChar;
    private String uris;
    private String eByteArray;



    public model_ETypes(
        String eLong,        LocalDate eDate,        String eBigInteger,        String eShort,        String eBigDecimal,        float eFloat,        float eDouble,        String eByte,        int eInt,        boolean eBoolean,        String eString,        String eChar,        String uris,        String eByteArray    ) {
        this.eLong = eLong;
        this.eDate = eDate;
        this.eBigInteger = eBigInteger;
        this.eShort = eShort;
        this.eBigDecimal = eBigDecimal;
        this.eFloat = eFloat;
        this.eDouble = eDouble;
        this.eByte = eByte;
        this.eInt = eInt;
        this.eBoolean = eBoolean;
        this.eString = eString;
        this.eChar = eChar;
        this.uris = uris;
        this.eByteArray = eByteArray;
    }


    public String getElong() {
        return eLong;
    }

    public void setElong(String eLong) {
        this.eLong = eLong;
    }
    public LocalDate getEdate() {
        return eDate;
    }

    public void setEdate(LocalDate eDate) {
        this.eDate = eDate;
    }
    public String getEbiginteger() {
        return eBigInteger;
    }

    public void setEbiginteger(String eBigInteger) {
        this.eBigInteger = eBigInteger;
    }
    public String getEshort() {
        return eShort;
    }

    public void setEshort(String eShort) {
        this.eShort = eShort;
    }
    public String getEbigdecimal() {
        return eBigDecimal;
    }

    public void setEbigdecimal(String eBigDecimal) {
        this.eBigDecimal = eBigDecimal;
    }
    public float getEfloat() {
        return eFloat;
    }

    public void setEfloat(float eFloat) {
        this.eFloat = eFloat;
    }
    public float getEdouble() {
        return eDouble;
    }

    public void setEdouble(float eDouble) {
        this.eDouble = eDouble;
    }
    public String getEbyte() {
        return eByte;
    }

    public void setEbyte(String eByte) {
        this.eByte = eByte;
    }
    public int getEint() {
        return eInt;
    }

    public void setEint(int eInt) {
        this.eInt = eInt;
    }
    public boolean getEboolean() {
        return eBoolean;
    }

    public void setEboolean(boolean eBoolean) {
        this.eBoolean = eBoolean;
    }
    public String getEstring() {
        return eString;
    }

    public void setEstring(String eString) {
        this.eString = eString;
    }
    public String getEchar() {
        return eChar;
    }

    public void setEchar(String eChar) {
        this.eChar = eChar;
    }
    public String getUris() {
        return uris;
    }

    public void setUris(String uris) {
        this.uris = uris;
    }
    public String getEbytearray() {
        return eByteArray;
    }

    public void setEbytearray(String eByteArray) {
        this.eByteArray = eByteArray;
    }


}