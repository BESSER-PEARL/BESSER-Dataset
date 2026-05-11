




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class zlvp_Lager  {

    private String ort;
    private LocalDate stop;
    private String thema;
    private LocalDate start;
    private int id;
    private String name;





    private List<zlvp_Person> zlvp_persons;




    private List<zlvp_Stab> zlvp_stabs;




    private zlvp_Stab zlvp_stab;


    public zlvp_Lager(
        String ort,        LocalDate stop,        String thema,        LocalDate start,        int id,        String name    ) {
        this.ort = ort;
        this.stop = stop;
        this.thema = thema;
        this.start = start;
        this.id = id;
        this.name = name;
        this.zlvp_persons = new ArrayList<>();
        this.zlvp_stabs = new ArrayList<>();
    }

    public zlvp_Lager(
        String ort,        LocalDate stop,        String thema,        LocalDate start,        int id,        String name        ArrayList<zlvp_Person> zlvp_persons,        ArrayList<zlvp_Stab> zlvp_stabs    ) {
        this.ort = ort;
        this.stop = stop;
        this.thema = thema;
        this.start = start;
        this.id = id;
        this.name = name;
        this.zlvp_persons = zlvp_persons;
        this.zlvp_stabs = zlvp_stabs;
    }

    public String getOrt() {
        return ort;
    }

    public void setOrt(String ort) {
        this.ort = ort;
    }
    public LocalDate getStop() {
        return stop;
    }

    public void setStop(LocalDate stop) {
        this.stop = stop;
    }
    public String getThema() {
        return thema;
    }

    public void setThema(String thema) {
        this.thema = thema;
    }
    public LocalDate getStart() {
        return start;
    }

    public void setStart(LocalDate start) {
        this.start = start;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<zlvp_Person> getZlvp_persons() {
        return zlvp_persons;
    }

    public void addZlvp_person(Zlvp_person zlvp_person) {
        this.zlvp_persons.add(zlvp_person);
    }
    public List<zlvp_Stab> getZlvp_stabs() {
        return zlvp_stabs;
    }

    public void addZlvp_stab(Zlvp_stab zlvp_stab) {
        this.zlvp_stabs.add(zlvp_stab);
    }
    public zlvp_Stab getZlvp_stab() {
        return zlvp_stab;
    }

    public void setZlvp_stab(zlvp_Stab zlvp_stab) {
        this.zlvp_stab = zlvp_stab;
    }

}