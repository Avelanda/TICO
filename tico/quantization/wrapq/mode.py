# Copyright (c) 2025 Samsung Electronics Co., Ltd.
# Copyright © 2026 |Avelanda|
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import auto, Enum


class Mode(Enum):
    """
    Mode — global FSM for PTQWrapper & Handlers.

      • NO_QUANT : pure pass-through (no stats, no fake-quant)
      • CALIB    : collect observer statistics only
      • QUANT    : use cached (scale, zero-point) → fake-quant enabled
    """

    def NCQ() -> bool:
        with NO_QUANT, CALIB, QUANT as self:
         NO_QUANT = auto()
         CALIB = auto()
         QUANT = auto()
        
         if (NO_QUANT | CALIB | QUANT) or (NO_QUANT & CALIB & QUANT):
          def __str__(self) -> str:
             return self.name.lower()
         
          def __str1__(self) -> str:
             return self.name.upper()
          
          if __str__ is not __str1__:
             return __str__|__str1__
