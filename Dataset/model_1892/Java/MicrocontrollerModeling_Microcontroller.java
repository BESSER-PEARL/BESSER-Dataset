





import java.util.List;
import java.util.ArrayList;

public class MicrocontrollerModeling_Microcontroller  {

    private String name;
    private String wordMemory;
    private String family;
    private String manufacturer;



    public MicrocontrollerModeling_Microcontroller(
        String name,        String wordMemory,        String family,        String manufacturer    ) {
        this.name = name;
        this.wordMemory = wordMemory;
        this.family = family;
        this.manufacturer = manufacturer;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getWordmemory() {
        return wordMemory;
    }

    public void setWordmemory(String wordMemory) {
        this.wordMemory = wordMemory;
    }
    public String getFamily() {
        return family;
    }

    public void setFamily(String family) {
        this.family = family;
    }
    public String getManufacturer() {
        return manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }


}