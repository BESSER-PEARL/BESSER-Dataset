





import java.util.List;
import java.util.ArrayList;

public class cs_CSTransform  {

    private float m00;
    private float m21;
    private float m20;
    private float m10;
    private float m01;
    private float m22;
    private float m02;
    private float m12;
    private float m11;





    private cs_CSElement cs_cselement;


    public cs_CSTransform(
        float m00,        float m21,        float m20,        float m10,        float m01,        float m22,        float m02,        float m12,        float m11    ) {
        this.m00 = m00;
        this.m21 = m21;
        this.m20 = m20;
        this.m10 = m10;
        this.m01 = m01;
        this.m22 = m22;
        this.m02 = m02;
        this.m12 = m12;
        this.m11 = m11;
    }


    public float getM00() {
        return m00;
    }

    public void setM00(float m00) {
        this.m00 = m00;
    }
    public float getM21() {
        return m21;
    }

    public void setM21(float m21) {
        this.m21 = m21;
    }
    public float getM20() {
        return m20;
    }

    public void setM20(float m20) {
        this.m20 = m20;
    }
    public float getM10() {
        return m10;
    }

    public void setM10(float m10) {
        this.m10 = m10;
    }
    public float getM01() {
        return m01;
    }

    public void setM01(float m01) {
        this.m01 = m01;
    }
    public float getM22() {
        return m22;
    }

    public void setM22(float m22) {
        this.m22 = m22;
    }
    public float getM02() {
        return m02;
    }

    public void setM02(float m02) {
        this.m02 = m02;
    }
    public float getM12() {
        return m12;
    }

    public void setM12(float m12) {
        this.m12 = m12;
    }
    public float getM11() {
        return m11;
    }

    public void setM11(float m11) {
        this.m11 = m11;
    }

    public cs_CSElement getCs_cselement() {
        return cs_cselement;
    }

    public void setCs_cselement(cs_CSElement cs_cselement) {
        this.cs_cselement = cs_cselement;
    }

}