




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Lims_Run  {

    private LocalDate date;
    private String name;





    private Lims_Sequencer lims_sequencer;




    private Lims_Sequencer lims_sequencer;


    public Lims_Run(
        LocalDate date,        String name    ) {
        this.date = date;
        this.name = name;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Lims_Sequencer getLims_sequencer() {
        return lims_sequencer;
    }

    public void setLims_sequencer(Lims_Sequencer lims_sequencer) {
        this.lims_sequencer = lims_sequencer;
    }
    public Lims_Sequencer getLims_sequencer() {
        return lims_sequencer;
    }

    public void setLims_sequencer(Lims_Sequencer lims_sequencer) {
        this.lims_sequencer = lims_sequencer;
    }

}