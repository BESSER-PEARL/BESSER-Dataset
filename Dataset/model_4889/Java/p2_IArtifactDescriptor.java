





import java.util.List;
import java.util.ArrayList;

public class p2_IArtifactDescriptor  {






    private p2_ArtifactsByKey p2_artifactsbykey;




    private p2_IArtifactKey p2_iartifactkey;


    public p2_IArtifactDescriptor(
    ) {
    }



    public p2_ArtifactsByKey getP2_artifactsbykey() {
        return p2_artifactsbykey;
    }

    public void setP2_artifactsbykey(p2_ArtifactsByKey p2_artifactsbykey) {
        this.p2_artifactsbykey = p2_artifactsbykey;
    }
    public p2_IArtifactKey getP2_iartifactkey() {
        return p2_iartifactkey;
    }

    public void setP2_iartifactkey(p2_IArtifactKey p2_iartifactkey) {
        this.p2_iartifactkey = p2_iartifactkey;
    }

}