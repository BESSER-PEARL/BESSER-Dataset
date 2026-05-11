





import java.util.List;
import java.util.ArrayList;

public class syswbeff106prepa_Workbench  {






    private List<syswbeff106prepa_PatternCatalog> syswbeff106prepa_patterncatalogs;




    private syswbeff106prepa_System syswbeff106prepa_system;


    public syswbeff106prepa_Workbench(
    ) {
        this.syswbeff106prepa_patterncatalogs = new ArrayList<>();
    }

    public syswbeff106prepa_Workbench(
        ArrayList<syswbeff106prepa_PatternCatalog> syswbeff106prepa_patterncatalogs    ) {
        this.syswbeff106prepa_patterncatalogs = syswbeff106prepa_patterncatalogs;
    }


    public List<syswbeff106prepa_PatternCatalog> getSyswbeff106prepa_patterncatalogs() {
        return syswbeff106prepa_patterncatalogs;
    }

    public void addSyswbeff106prepa_patterncatalog(Syswbeff106prepa_patterncatalog syswbeff106prepa_patterncatalog) {
        this.syswbeff106prepa_patterncatalogs.add(syswbeff106prepa_patterncatalog);
    }
    public syswbeff106prepa_System getSyswbeff106prepa_system() {
        return syswbeff106prepa_system;
    }

    public void setSyswbeff106prepa_system(syswbeff106prepa_System syswbeff106prepa_system) {
        this.syswbeff106prepa_system = syswbeff106prepa_system;
    }

}