





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_StatusBit  {

    private String bitName;
    private int bitNo;





    private MachineLibrary_StausBits machinelibrary_stausbits;


    public MachineLibrary_StatusBit(
        String bitName,        int bitNo    ) {
        this.bitName = bitName;
        this.bitNo = bitNo;
    }


    public String getBitname() {
        return bitName;
    }

    public void setBitname(String bitName) {
        this.bitName = bitName;
    }
    public int getBitno() {
        return bitNo;
    }

    public void setBitno(int bitNo) {
        this.bitNo = bitNo;
    }

    public MachineLibrary_StausBits getMachinelibrary_stausbits() {
        return machinelibrary_stausbits;
    }

    public void setMachinelibrary_stausbits(MachineLibrary_StausBits machinelibrary_stausbits) {
        this.machinelibrary_stausbits = machinelibrary_stausbits;
    }

}