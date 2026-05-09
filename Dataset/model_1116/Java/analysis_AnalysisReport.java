




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class analysis_AnalysisReport  {

    private String algorithm;
    private LocalDate date;



    public analysis_AnalysisReport(
        String algorithm,        LocalDate date    ) {
        this.algorithm = algorithm;
        this.date = date;
    }


    public String getAlgorithm() {
        return algorithm;
    }

    public void setAlgorithm(String algorithm) {
        this.algorithm = algorithm;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }


}