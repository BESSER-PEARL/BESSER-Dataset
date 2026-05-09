





import java.util.List;
import java.util.ArrayList;

public class pycom_Board  {

    private String boardType;
    private int communicationRate;
    private String name;





    private pycom_System pycom_system;




    private List<pycom_Library> pycom_librarys;


    public pycom_Board(
        String boardType,        int communicationRate,        String name    ) {
        this.boardType = boardType;
        this.communicationRate = communicationRate;
        this.name = name;
        this.pycom_librarys = new ArrayList<>();
    }

    public pycom_Board(
        String boardType,        int communicationRate,        String name        ArrayList<pycom_Library> pycom_librarys    ) {
        this.boardType = boardType;
        this.communicationRate = communicationRate;
        this.name = name;
        this.pycom_librarys = pycom_librarys;
    }

    public String getBoardtype() {
        return boardType;
    }

    public void setBoardtype(String boardType) {
        this.boardType = boardType;
    }
    public int getCommunicationrate() {
        return communicationRate;
    }

    public void setCommunicationrate(int communicationRate) {
        this.communicationRate = communicationRate;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pycom_System getPycom_system() {
        return pycom_system;
    }

    public void setPycom_system(pycom_System pycom_system) {
        this.pycom_system = pycom_system;
    }
    public List<pycom_Library> getPycom_librarys() {
        return pycom_librarys;
    }

    public void addPycom_library(Pycom_library pycom_library) {
        this.pycom_librarys.add(pycom_library);
    }

}