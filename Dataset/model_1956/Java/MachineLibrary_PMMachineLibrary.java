





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_PMMachineLibrary  {

    private float libraryVersion;
    private String libraryVersionRemark;



    public MachineLibrary_PMMachineLibrary(
        float libraryVersion,        String libraryVersionRemark    ) {
        this.libraryVersion = libraryVersion;
        this.libraryVersionRemark = libraryVersionRemark;
    }


    public float getLibraryversion() {
        return libraryVersion;
    }

    public void setLibraryversion(float libraryVersion) {
        this.libraryVersion = libraryVersion;
    }
    public String getLibraryversionremark() {
        return libraryVersionRemark;
    }

    public void setLibraryversionremark(String libraryVersionRemark) {
        this.libraryVersionRemark = libraryVersionRemark;
    }


}