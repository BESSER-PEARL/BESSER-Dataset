





import java.util.List;
import java.util.ArrayList;

public class PSM_ArtifactElement  {

    private String ParentProjectName;
    private String ArtifactFileName;
    private String GeneratingLinesOfCode;



    public PSM_ArtifactElement(
        String ParentProjectName,        String ArtifactFileName,        String GeneratingLinesOfCode    ) {
        this.ParentProjectName = ParentProjectName;
        this.ArtifactFileName = ArtifactFileName;
        this.GeneratingLinesOfCode = GeneratingLinesOfCode;
    }


    public String getParentprojectname() {
        return ParentProjectName;
    }

    public void setParentprojectname(String ParentProjectName) {
        this.ParentProjectName = ParentProjectName;
    }
    public String getArtifactfilename() {
        return ArtifactFileName;
    }

    public void setArtifactfilename(String ArtifactFileName) {
        this.ArtifactFileName = ArtifactFileName;
    }
    public String getGeneratinglinesofcode() {
        return GeneratingLinesOfCode;
    }

    public void setGeneratinglinesofcode(String GeneratingLinesOfCode) {
        this.GeneratingLinesOfCode = GeneratingLinesOfCode;
    }


}