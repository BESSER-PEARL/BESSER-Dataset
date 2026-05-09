





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_Parameter  {

    private String parameterV0;
    private int parameterParaLen;
    private int parameterMin;
    private String parameterName;
    private String parameterT2;
    private String parameterV1;
    private String parameterT1;
    private String parameterType;
    private String parameterV;
    private int parameterMax;
    private String parameterConfig;





    private MachineLibrary_Parameters machinelibrary_parameters;


    public MachineLibrary_Parameter(
        String parameterV0,        int parameterParaLen,        int parameterMin,        String parameterName,        String parameterT2,        String parameterV1,        String parameterT1,        String parameterType,        String parameterV,        int parameterMax,        String parameterConfig    ) {
        this.parameterV0 = parameterV0;
        this.parameterParaLen = parameterParaLen;
        this.parameterMin = parameterMin;
        this.parameterName = parameterName;
        this.parameterT2 = parameterT2;
        this.parameterV1 = parameterV1;
        this.parameterT1 = parameterT1;
        this.parameterType = parameterType;
        this.parameterV = parameterV;
        this.parameterMax = parameterMax;
        this.parameterConfig = parameterConfig;
    }


    public String getParameterv0() {
        return parameterV0;
    }

    public void setParameterv0(String parameterV0) {
        this.parameterV0 = parameterV0;
    }
    public int getParameterparalen() {
        return parameterParaLen;
    }

    public void setParameterparalen(int parameterParaLen) {
        this.parameterParaLen = parameterParaLen;
    }
    public int getParametermin() {
        return parameterMin;
    }

    public void setParametermin(int parameterMin) {
        this.parameterMin = parameterMin;
    }
    public String getParametername() {
        return parameterName;
    }

    public void setParametername(String parameterName) {
        this.parameterName = parameterName;
    }
    public String getParametert2() {
        return parameterT2;
    }

    public void setParametert2(String parameterT2) {
        this.parameterT2 = parameterT2;
    }
    public String getParameterv1() {
        return parameterV1;
    }

    public void setParameterv1(String parameterV1) {
        this.parameterV1 = parameterV1;
    }
    public String getParametert1() {
        return parameterT1;
    }

    public void setParametert1(String parameterT1) {
        this.parameterT1 = parameterT1;
    }
    public String getParametertype() {
        return parameterType;
    }

    public void setParametertype(String parameterType) {
        this.parameterType = parameterType;
    }
    public String getParameterv() {
        return parameterV;
    }

    public void setParameterv(String parameterV) {
        this.parameterV = parameterV;
    }
    public int getParametermax() {
        return parameterMax;
    }

    public void setParametermax(int parameterMax) {
        this.parameterMax = parameterMax;
    }
    public String getParameterconfig() {
        return parameterConfig;
    }

    public void setParameterconfig(String parameterConfig) {
        this.parameterConfig = parameterConfig;
    }

    public MachineLibrary_Parameters getMachinelibrary_parameters() {
        return machinelibrary_parameters;
    }

    public void setMachinelibrary_parameters(MachineLibrary_Parameters machinelibrary_parameters) {
        this.machinelibrary_parameters = machinelibrary_parameters;
    }

}