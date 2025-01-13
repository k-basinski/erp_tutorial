# %%
import mne
# %%
fdir = '/Users/kbas/sci_data/multifeature/'
fname = 'mf_02_04092024_Gosia.bdf'

raw = mne.io.read_raw_bdf(fdir+fname)

# %%
raw.plot()
# %%
raw.crop(0, 60)
raw.resample(100, n_jobs=-1)

# %%
raw.plot()
# %%
raw.save('data/raw.fif')
# %%``
# epochs
epochs = mne.read_epochs(fdir+'preprocessed/1-epo.fif')
epochs.set_eeg_reference('REST')
# %%
epochs['harmonic/pitch']
# %%
epochs['harmonic/std']
# %%
ep = epochs['harmonic/pitch']
ep = epochs['harmonic/pitch'].copy().resample(100, n_jobs=-1)
ed = epochs['harmonic/std'].copy().resample(100, n_jobs=-1)
ep.save('data/deviants-epo.fif', overwrite=True)
ed.save('data/standards-epo.fif', overwrite=True)
# %%
ep.info
# %%
ep.plot()
# %%
ep.average().plot()
# %%
ed.average().plot()
# %%
ed.info
# %%
