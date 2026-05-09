





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_TransferFileSection  {

    private int transferSeq;
    private String transferSection;
    private String transferFile;





    private MachineLibrary_Transfer machinelibrary_transfer;


    public MachineLibrary_TransferFileSection(
        int transferSeq,        String transferSection,        String transferFile    ) {
        this.transferSeq = transferSeq;
        this.transferSection = transferSection;
        this.transferFile = transferFile;
    }


    public int getTransferseq() {
        return transferSeq;
    }

    public void setTransferseq(int transferSeq) {
        this.transferSeq = transferSeq;
    }
    public String getTransfersection() {
        return transferSection;
    }

    public void setTransfersection(String transferSection) {
        this.transferSection = transferSection;
    }
    public String getTransferfile() {
        return transferFile;
    }

    public void setTransferfile(String transferFile) {
        this.transferFile = transferFile;
    }

    public MachineLibrary_Transfer getMachinelibrary_transfer() {
        return machinelibrary_transfer;
    }

    public void setMachinelibrary_transfer(MachineLibrary_Transfer machinelibrary_transfer) {
        this.machinelibrary_transfer = machinelibrary_transfer;
    }

}